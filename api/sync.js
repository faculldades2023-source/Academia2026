export default async function handler(req, res) {
  // CORS Headers
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
  );

  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  const { uid } = req.query;
  if (!uid) {
    return res.status(400).json({ error: 'Missing uid parameter' });
  }

  const kvUrl = process.env.KV_REST_API_URL;
  const kvToken = process.env.KV_REST_API_TOKEN;

  if (!kvUrl || !kvToken) {
    return res.status(500).json({ error: 'Vercel KV environment variables are not configured' });
  }

  const key = `user:${uid}`;

  try {
    if (req.method === 'GET') {
      const response = await fetch(kvUrl, {
        headers: {
          Authorization: `Bearer ${kvToken}`
        },
        body: JSON.stringify(['GET', key]),
        method: 'POST'
      });
      const data = await response.json();
      const val = data.result ? JSON.parse(data.result) : null;
      return res.status(200).json({ state: val });
    }

    if (req.method === 'POST') {
      const { state } = req.body;
      if (!state) {
        return res.status(400).json({ error: 'Missing state body' });
      }
      
      await fetch(kvUrl, {
        headers: {
          Authorization: `Bearer ${kvToken}`
        },
        body: JSON.stringify(['SET', key, JSON.stringify(state)]),
        method: 'POST'
      });
      return res.status(200).json({ success: true });
    }

    return res.status(405).json({ error: 'Method not allowed' });
  } catch (error) {
    console.error("KV API Error:", error);
    return res.status(500).json({ error: error.message });
  }
}
