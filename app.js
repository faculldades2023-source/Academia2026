document.addEventListener('DOMContentLoaded', () => {

  function vectorSvg(type, color) {
    const common = `style="color:${color}"`;
    const svgs = {
      bench: `<svg width="100%" height="100%" viewBox="0 0 120 120" fill="none" ${common}><g class="v-breath"><rect x="15" y="80" width="90" height="10" rx="4" fill="#2a2a3a"/><path d="M35 80 L20 80 L20 105 L30 105" stroke="#1e1e2c" stroke-width="10" stroke-linejoin="round" fill="none"/><circle cx="85" cy="74" r="10" fill="#ffb48f"/><rect x="30" y="68" width="50" height="18" rx="9" fill="currentColor"/><g class="v-lift"><path d="M70 75 L65 50" stroke="#ffb48f" stroke-width="8" stroke-linecap="round"/><rect x="15" y="46" width="90" height="6" rx="3" fill="#888"/><rect x="25" y="30" width="8" height="38" rx="2" fill="#222"/><rect x="87" y="30" width="8" height="38" rx="2" fill="#222"/></g></g></svg>`,
      squat: `<svg width="100%" height="100%" viewBox="0 0 120 120" fill="none" ${common}><g class="v-squat-anim"><g class="v-lift"><circle cx="60" cy="25" r="10" fill="#ffb48f"/><rect x="50" y="37" width="20" height="35" rx="8" fill="currentColor"/><path d="M55 42 L40 50 L45 30" stroke="#ffb48f" stroke-width="7" stroke-linecap="round" fill="none"/><path d="M65 42 L80 50 L75 30" stroke="#ffb48f" stroke-width="7" stroke-linecap="round" fill="none"/><rect x="15" y="27" width="90" height="6" rx="3" fill="#888"/><rect x="20" y="10" width="10" height="40" rx="3" fill="#222"/><rect x="90" y="10" width="10" height="40" rx="3" fill="#222"/></g><path d="M55 70 L45 95 L55 115" stroke="#1e1e2c" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M65 70 L75 95 L65 115" stroke="#1e1e2c" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/></g></svg>`,
      lat: `<svg width="100%" height="100%" viewBox="0 0 120 120" fill="none" ${common}><g class="v-breath"><rect x="40" y="80" width="40" height="10" rx="4" fill="#2a2a3a"/><rect x="55" y="90" width="10" height="30" fill="#2a2a3a"/><path d="M50 80 L40 100 L50 115" stroke="#1e1e2c" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="60" cy="35" r="10" fill="#ffb48f"/><rect x="50" y="47" width="20" height="35" rx="8" fill="currentColor"/><g class="v-pull"><path d="M55 52 L35 25" stroke="#ffb48f" stroke-width="7" stroke-linecap="round"/><path d="M65 52 L85 25" stroke="#ffb48f" stroke-width="7" stroke-linecap="round"/><rect x="20" y="20" width="80" height="6" rx="3" fill="#888"/></g><rect x="58" y="-10" width="4" height="40" fill="#6b6b88"/></g></svg>`,
      row: `<svg width="100%" height="100%" viewBox="0 0 120 120" fill="none" ${common}><g class="v-breath"><rect x="20" y="80" width="30" height="10" rx="4" fill="#2a2a3a"/><rect x="80" y="70" width="10" height="40" rx="4" fill="#2a2a3a"/><path d="M40 80 L60 80 L75 95" stroke="#1e1e2c" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="45" cy="35" r="10" fill="#ffb48f"/><rect x="35" y="47" width="20" height="35" rx="8" fill="currentColor"/><g class="v-row"><path d="M45 55 L75 65" stroke="#ffb48f" stroke-width="8" stroke-linecap="round"/><circle cx="78" cy="65" r="5" fill="#888"/><line x1="78" y1="65" x2="100" y2="65" stroke="#6b6b88" stroke-width="4"/></g></g></svg>`,
      curl: `<svg width="100%" height="100%" viewBox="0 0 120 120" fill="none" ${common}><g class="v-breath"><path d="M55 70 L55 110" stroke="#1e1e2c" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M65 70 L65 110" stroke="#1e1e2c" stroke-width="12" stroke-linecap="round" fill="none"/><circle cx="60" cy="25" r="10" fill="#ffb48f"/><rect x="50" y="37" width="20" height="35" rx="8" fill="currentColor"/><line x1="60" y1="42" x2="60" y2="65" stroke="#ffb48f" stroke-width="7" stroke-linecap="round"/><g class="v-curl-arm"><line x1="60" y1="65" x2="85" y2="65" stroke="#ffb48f" stroke-width="7" stroke-linecap="round"/><rect x="80" y="55" width="10" height="20" rx="3" fill="#222"/></g></g></svg>`,
      legpress: `<svg width="100%" height="100%" viewBox="0 0 120 120" fill="none" ${common}><g class="v-breath"><rect x="20" y="60" width="60" height="12" rx="4" fill="#2a2a3a" transform="rotate(-30 50 70)"/><circle cx="35" cy="55" r="10" fill="#ffb48f"/><rect x="25" y="67" width="20" height="35" rx="8" fill="currentColor" transform="rotate(-30 35 67)"/><g class="v-legpress"><path d="M60 85 L80 80 L90 50" stroke="#ffb48f" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" fill="none"/><rect x="85" y="20" width="10" height="50" rx="3" fill="#888"/><rect x="95" y="30" width="15" height="30" rx="2" fill="#222"/></g></g></svg>`,
      shoulder: `<svg width="100%" height="100%" viewBox="0 0 120 120" fill="none" ${common}><g class="v-breath"><rect x="50" y="80" width="20" height="10" rx="4" fill="#2a2a3a"/><rect x="40" y="50" width="10" height="40" rx="4" fill="#2a2a3a"/><path d="M55 80 L55 110 L65 110" stroke="#1e1e2c" stroke-width="12" stroke-linejoin="round" fill="none"/><circle cx="60" cy="25" r="10" fill="#ffb48f"/><rect x="50" y="37" width="20" height="35" rx="8" fill="currentColor"/><g class="v-lift"><path d="M55 42 L35 42 L35 20" stroke="#ffb48f" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M65 42 L85 42 L85 20" stroke="#ffb48f" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><rect x="25" y="10" width="20" height="10" rx="3" fill="#222"/><rect x="75" y="10" width="20" height="10" rx="3" fill="#222"/></g></g></svg>`,
      pecdeck: `<svg width="100%" height="100%" viewBox="0 0 120 120" fill="none" ${common}><g class="v-breath"><rect x="50" y="40" width="20" height="50" rx="4" fill="#2a2a3a"/><circle cx="60" cy="25" r="10" fill="#ffb48f"/><rect x="50" y="37" width="20" height="35" rx="8" fill="currentColor"/><g class="v-pecdeck"><path d="M55 45 L30 45 L30 20" stroke="#ffb48f" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M65 45 L90 45 L90 20" stroke="#ffb48f" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/></g></g></svg>`,
      tricep: `<svg width="100%" height="100%" viewBox="0 0 120 120" fill="none" ${common}><g class="v-breath"><path d="M55 70 L55 110" stroke="#1e1e2c" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M65 70 L65 110" stroke="#1e1e2c" stroke-width="12" stroke-linecap="round" fill="none"/><circle cx="60" cy="25" r="10" fill="#ffb48f"/><rect x="50" y="37" width="20" height="35" rx="8" fill="currentColor"/><rect x="90" y="10" width="10" height="100" rx="4" fill="#2a2a3a"/><line x1="60" y1="45" x2="70" y2="65" stroke="#ffb48f" stroke-width="7" stroke-linecap="round"/><g class="v-tricep-arm"><line x1="70" y1="65" x2="85" y2="45" stroke="#ffb48f" stroke-width="7" stroke-linecap="round"/><line x1="85" y1="45" x2="95" y2="15" stroke="#6b6b88" stroke-width="3"/></g></g></svg>`,
      lateral: `<svg width="100%" height="100%" viewBox="0 0 120 120" fill="none" ${common}><g class="v-breath"><path d="M55 70 L55 110" stroke="#1e1e2c" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M65 70 L65 110" stroke="#1e1e2c" stroke-width="12" stroke-linecap="round" fill="none"/><circle cx="60" cy="25" r="10" fill="#ffb48f"/><rect x="50" y="37" width="20" height="35" rx="8" fill="currentColor"/><g class="v-lateral-arm-l"><line x1="50" y1="42" x2="30" y2="60" stroke="#ffb48f" stroke-width="7" stroke-linecap="round"/><rect x="25" y="55" width="10" height="15" rx="2" fill="#222"/></g><g class="v-lateral-arm-r"><line x1="70" y1="42" x2="90" y2="60" stroke="#ffb48f" stroke-width="7" stroke-linecap="round"/><rect x="85" y="55" width="10" height="15" rx="2" fill="#222"/></g></g></svg>`,
      shrug: `<svg width="100%" height="100%" viewBox="0 0 120 120" fill="none" ${common}><g class="v-shrug-anim"><path d="M55 70 L55 110" stroke="#1e1e2c" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M65 70 L65 110" stroke="#1e1e2c" stroke-width="12" stroke-linecap="round" fill="none"/><circle cx="60" cy="25" r="10" fill="#ffb48f"/><rect x="50" y="37" width="20" height="35" rx="8" fill="currentColor"/><g class="v-shrug-arms"><line x1="50" y1="42" x2="40" y2="70" stroke="#ffb48f" stroke-width="7" stroke-linecap="round"/><line x1="70" y1="42" x2="80" y2="70" stroke="#ffb48f" stroke-width="7" stroke-linecap="round"/><rect x="35" y="65" width="10" height="20" rx="2" fill="#222"/><rect x="75" y="65" width="10" height="20" rx="2" fill="#222"/></g></g></svg>`,
      calf: `<svg width="100%" height="100%" viewBox="0 0 120 120" fill="none" ${common}><g class="v-calf-anim"><path d="M55 70 L55 110" stroke="#1e1e2c" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M65 70 L65 110" stroke="#1e1e2c" stroke-width="12" stroke-linecap="round" fill="none"/><circle cx="60" cy="25" r="10" fill="#ffb48f"/><rect x="50" y="37" width="20" height="35" rx="8" fill="currentColor"/><line x1="50" y1="42" x2="40" y2="60" stroke="#ffb48f" stroke-width="7" stroke-linecap="round"/><line x1="70" y1="42" x2="80" y2="60" stroke="#ffb48f" stroke-width="7" stroke-linecap="round"/></g><rect x="40" y="110" width="40" height="10" rx="3" fill="#2a2a3a"/></svg>`,
      abs: `<svg width="100%" height="100%" viewBox="0 0 120 120" fill="none" ${common}><g class="v-abs-anim"><rect x="20" y="90" width="80" height="10" rx="4" fill="#2a2a3a"/><path d="M70 90 L85 75 L100 90" stroke="#1e1e2c" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="25" cy="80" r="10" fill="#ffb48f"/><rect x="35" y="75" width="35" height="15" rx="7" fill="currentColor"/><path d="M55 80 L40 70 L25 75" stroke="#ffb48f" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/></g></svg>`,
      cardio: `<svg width="100%" height="100%" viewBox="0 0 120 120" fill="none" ${common}><g class="v-cardio"><rect x="20" y="100" width="80" height="10" rx="5" fill="#2a2a3a"/><rect x="80" y="50" width="8" height="50" rx="4" fill="#6b6b88"/><rect x="70" y="45" width="20" height="10" rx="3" fill="#2a2a3a"/><circle cx="50" cy="25" r="10" fill="#ffb48f"/><rect x="40" y="37" width="20" height="30" rx="8" fill="currentColor"/><g class="v-run-leg-1"><line x1="50" y1="65" x2="40" y2="95" stroke="#1e1e2c" stroke-width="10" stroke-linecap="round"/></g><g class="v-run-leg-2"><line x1="50" y1="65" x2="60" y2="95" stroke="#1e1e2c" stroke-width="10" stroke-linecap="round"/></g><g class="v-run-arm-1"><line x1="50" y1="45" x2="30" y2="60" stroke="#ffb48f" stroke-width="7" stroke-linecap="round"/></g><g class="v-run-arm-2"><line x1="50" y1="45" x2="70" y2="55" stroke="#ffb48f" stroke-width="7" stroke-linecap="round"/></g></g></svg>`,
    };
    return svgs[type] || svgs.bench;
  }

  // --- STATE ---
  let state = {
    streak: 0,
    bestStreak: 0,
    weight: null,
    workouts: [],
    photos: [] // { date, src }
  };

  // --- NAVIGATION & SIDEBAR ---
  const views = document.querySelectorAll('.view');
  const navBtns = document.querySelectorAll('.nav-btn[data-view], .sidebar-link[data-view]');
  const sidebarOverlay = document.getElementById('sidebar-overlay');
  
  function switchView(viewId) {
    views.forEach(v => v.classList.remove('active'));
    document.getElementById('view-' + viewId).classList.add('active');
    
    navBtns.forEach(btn => {
      if(btn.dataset.view === viewId) btn.classList.add('active');
      else btn.classList.remove('active');
    });

    sidebarOverlay.classList.add('hidden'); // Close sidebar if open
    
    // Trigger specific render logic
    if(viewId === 'calendar') renderCalendar();
    if(viewId === 'stats') renderStats();
    if(viewId === 'diet') calcDiet();
    if(viewId === 'exercises') renderExercises('peito');
  }

  navBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const view = e.currentTarget.dataset.view;
      if(view) switchView(view);
    });
  });

  // Sidebar toggles
  document.getElementById('btn-menu').addEventListener('click', () => {
    sidebarOverlay.classList.remove('hidden');
    setTimeout(() => sidebarOverlay.classList.add('active'), 10);
  });
  document.getElementById('close-sidebar').addEventListener('click', () => {
    sidebarOverlay.classList.remove('active');
    setTimeout(() => sidebarOverlay.classList.add('hidden'), 300);
  });

  // --- MODALS ---
  function openModal(id) {
    document.getElementById(id).classList.remove('hidden');
  }
  function closeModal(id) {
    document.getElementById(id).classList.add('hidden');
  }

  document.getElementById('nav-add-btn').addEventListener('click', () => openModal('overlay-workout'));
  document.getElementById('btn-quick-add').addEventListener('click', () => openModal('overlay-workout'));
  document.getElementById('close-workout').addEventListener('click', () => closeModal('overlay-workout'));
  
  document.getElementById('btn-add-ex').addEventListener('click', () => {
    closeModal('overlay-workout');
    openModal('overlay-exercise');
  });
  document.getElementById('close-ex').addEventListener('click', () => {
    closeModal('overlay-exercise');
    openModal('overlay-workout');
  });
  
  document.getElementById('close-ex-detail').addEventListener('click', () => closeModal('overlay-ex-detail'));

  // --- TOAST ---
  function showToast(msg, type = 'success') {
    const toast = document.getElementById('toast');
    toast.textContent = msg;
    toast.className = `toast ${type}`;
    toast.classList.remove('hidden');
    setTimeout(() => toast.classList.add('hidden'), 3000);
  }

  // --- CALENDAR LOGIC ---
  const calGrid = document.getElementById('calendar-grid');
  const calMonthYear = document.getElementById('cal-month-year');
  let currentDate = new Date();

  const calendarSchedule={
    1:'A', 4:'B', 5:'C', 6:'D', 7:'A', 8:'B', 11:'C', 12:'D', 13:'A', 14:'B', 15:'C',
    18:'D', 19:'A', 20:'B', 21:'C', 22:'D', 25:'A', 26:'B', 27:'C', 28:'D', 29:'A'
  };
  const calendarRest=[2,3,9,10,16,17,23,24,30,31];

  function renderCalendar() {
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();
    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    
    const monthNames = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'];
    calMonthYear.textContent = `${monthNames[month]} ${year}`;
    calGrid.innerHTML = '';

    for (let i = 0; i < firstDay; i++) {
      const emptyDiv = document.createElement('div');
      emptyDiv.className = 'cal-day cal-empty';
      calGrid.appendChild(emptyDiv);
    }

    const today = new Date();

    for (let i = 1; i <= daysInMonth; i++) {
      const key = calendarSchedule[i];
      const isRest = calendarRest.includes(i);
      
      const dayDiv = document.createElement('div');
      dayDiv.className = 'cal-day';
      if (year === today.getFullYear() && month === today.getMonth() && i === today.getDate()) {
        dayDiv.classList.add('today');
      }

      let content = `<div class="cal-date" style="color:${(year === today.getFullYear() && month === today.getMonth() && i === today.getDate()) ? 'var(--accent)' : 'var(--text)'}">${i}</div>`;
      
      if(key) {
        const colorMap = { A:'#3b82f6', B:'#7c3aed', C:'#f97316', D:'#10b981' };
        content += `<div class="cal-letter-wrap" style="background:${colorMap[key]}">${key}</div>`;
      } else if(isRest) {
        content += `<div class="cal-rest-wrap">Zzz</div>`;
      }
      
      if(!key && !isRest) {
        dayDiv.style.opacity = '0.5';
      }

      dayDiv.innerHTML = content;
      calGrid.appendChild(dayDiv);
    }
  }

  document.getElementById('cal-prev').addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() - 1);
    renderCalendar();
  });
  document.getElementById('cal-next').addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() + 1);
    renderCalendar();
  });

  // --- STATS LOGIC ---
  let chartsRendered = false;
  function renderStats() {
    if (chartsRendered) return;
    chartsRendered = true;

    // Radar Chart (Medidas Corporais)
    const ctxRadar = document.getElementById('chart-radar').getContext('2d');
    new Chart(ctxRadar, {
      type: 'radar',
      data: {
        labels: ['Peito', 'Costas', 'Braços', 'Pernas', 'Ombros', 'Abdômen'],
        datasets: [{
          label: 'Mês Atual',
          data: [100, 105, 38, 60, 115, 85],
          backgroundColor: 'rgba(124, 58, 237, 0.4)',
          borderColor: '#7c3aed',
          pointBackgroundColor: '#fff',
        }, {
          label: 'Mês Anterior',
          data: [98, 102, 36, 58, 110, 86],
          backgroundColor: 'rgba(249, 115, 22, 0.3)',
          borderColor: '#f97316',
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: { r: { ticks: { display: false }, grid: { color: 'rgba(255,255,255,0.1)' }, pointLabels: { color: '#a78bfa' } } },
        plugins: { legend: { labels: { color: '#e5e7eb' } } }
      }
    });

    // Volume Chart (Line)
    const ctxVol = document.getElementById('chart-volume').getContext('2d');
    new Chart(ctxVol, {
      type: 'line',
      data: {
        labels: ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4'],
        datasets: [{
          label: 'Supino (kg)',
          data: [60, 65, 65, 70],
          borderColor: '#3b82f6',
          tension: 0.3
        }, {
          label: 'Agachamento (kg)',
          data: [80, 85, 90, 95],
          borderColor: '#f97316',
          tension: 0.3
        }]
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        scales: {
          x: { grid: { display: false }, ticks: { color: '#9ca3af' } },
          y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9ca3af' } }
        },
        plugins: { legend: { labels: { color: '#e5e7eb' } } }
      }
    });
  }

  // --- DIET LOGIC ---
  function calcDiet() {
    let weight = parseFloat(document.getElementById('goal-weight').value) || 75;
    let phase = document.getElementById('goal-phase')?.value || 'bulking';
    
    let pro, carb, fat, kcal;

    if (phase === 'bulking') {
      pro = weight * 2.2;
      fat = weight * 1.0;
      kcal = weight * 35; // approx
      carb = (kcal - (pro * 4) - (fat * 9)) / 4;
    } else {
      pro = weight * 2.5;
      fat = weight * 0.8;
      kcal = weight * 25;
      carb = (kcal - (pro * 4) - (fat * 9)) / 4;
    }

    document.getElementById('calc-protein').textContent = Math.round(pro) + 'g';
    document.getElementById('calc-carb').textContent = Math.round(carb) + 'g';
    document.getElementById('calc-fat').textContent = Math.round(fat) + 'g';
    document.getElementById('calc-kcal').textContent = Math.round(kcal);
  }

  // --- EXERCISES LIBRARY ---
  const exerciseLibrary = [
    { cat: 'peito', name: 'Supino Reto na Máquina', muscle: 'Peito', machine: 'SENA Chest Press', exec: 'Sente-se com as costas apoiadas. Empurre as alças para frente estendendo os braços. Retorne controladamente.', err: ['Arquear excessivamente as costas', 'Soltar o peso rápido'], svgType: 'bench', color: '#3b82f6' },
    { cat: 'peito', name: 'Peck Deck (Voador)', muscle: 'Peito', machine: 'SENA Pectoral Fly', exec: 'Mantenha os cotovelos alinhados com o peito. Feche os braços contraindo o peitoral.', err: ['Usar muito impulso', 'Cotovelos muito baixos'], svgType: 'pecdeck', color: '#3b82f6' },
    { cat: 'costas', name: 'Puxada Frontal', muscle: 'Costas', machine: 'SENA Lat Pulldown', exec: 'Puxe a barra em direção ao peito superior, juntando as escápulas.', err: ['Puxar atrás da nuca', 'Balançar o tronco'], svgType: 'lat', color: '#7c3aed' },
    { cat: 'costas', name: 'Remada Sentada', muscle: 'Costas', machine: 'SENA Seated Row', exec: 'Puxe o triângulo até o abdômen, mantendo a postura ereta.', err: ['Curvar as costas'], svgType: 'row', color: '#7c3aed' },
    { cat: 'pernas', name: 'Leg Press 45º', muscle: 'Quadríceps/Glúteos', machine: 'SENA Leg Press', exec: 'Empurre a plataforma sem estender totalmente os joelhos.', err: ['Travar os joelhos no final', 'Descolar a lombar'], svgType: 'legpress', color: '#f97316' },
    { cat: 'pernas', name: 'Cadeira Extensora', muscle: 'Quadríceps', machine: 'SENA Leg Extension', exec: 'Estenda as pernas controladamente. Segure 1s no topo.', err: ['Levantar o quadril'], svgType: 'squat', color: '#f97316' },
    { cat: 'ombro', name: 'Desenvolvimento Máquina', muscle: 'Ombros', machine: 'SENA Shoulder Press', exec: 'Empurre o peso para cima. Desça até a altura das orelhas.', err: ['Descer demais forçando a articulação'], svgType: 'shoulder', color: '#10b981' },
    { cat: 'biceps', name: 'Rosca Scott Máquina', muscle: 'Bíceps', machine: 'SENA Preacher Curl', exec: 'Apoie o tríceps. Flexione os braços isolando o bíceps.', err: ['Tirar os cotovelos do apoio'], svgType: 'curl', color: '#eab308' },
    { cat: 'triceps', name: 'Tríceps Pulley', muscle: 'Tríceps', machine: 'Polia Alta', exec: 'Estenda os braços para baixo mantendo cotovelos colados ao corpo.', err: ['Afastar cotovelos'], svgType: 'tricep', color: '#ef4444' }
  ];

  function renderExercises(category) {
    const list = document.getElementById('exercises-library-list');
    list.innerHTML = '';
    const filtered = exerciseLibrary.filter(ex => ex.cat === category);
    
    filtered.forEach(ex => {
      const card = document.createElement('div');
      card.className = 'lib-card glass-card';
      card.innerHTML = `
        <div class="ex-anim" style="height:100px; background:var(--surface2); display:flex; align-items:center; justify-content:center;">
          ${vectorSvg(ex.svgType || 'bench', ex.color || '#7c3aed')}
        </div>
        <div class="lib-info">
          <div class="lib-name">${ex.name}</div>
          <div class="lib-muscle">${ex.muscle}</div>
        </div>
      `;
      card.addEventListener('click', () => openExerciseDetail(ex));
      list.appendChild(card);
    });
  }

  const exChips = document.querySelectorAll('#view-exercises .chip');
  exChips.forEach(chip => {
    chip.addEventListener('click', (e) => {
      exChips.forEach(c => c.classList.remove('active'));
      const btn = e.currentTarget;
      btn.classList.add('active');
      renderExercises(btn.dataset.excat);
    });
  });

  function openExerciseDetail(ex) {
    document.getElementById('tut-title').textContent = ex.name;
    document.getElementById('tut-machine').textContent = ex.machine;
    document.getElementById('tut-muscle').textContent = ex.muscle;
    document.getElementById('tut-execution').textContent = ex.exec;
    
    document.getElementById('tut-animation').innerHTML = vectorSvg(ex.svgType || 'bench', ex.color || '#7c3aed');

    const errList = document.getElementById('tut-errors');
    errList.innerHTML = '';
    ex.err.forEach(e => {
      const li = document.createElement('li');
      li.textContent = e;
      errList.appendChild(li);
    });

    openModal('overlay-ex-detail');
  }

  // --- PHOTOS UPLOAD ---
  const photoInput = document.getElementById('photo-upload');
  const photosGrid = document.getElementById('photos-grid');
  const photoSlider = document.getElementById('photo-slider');

  document.getElementById('btn-add-photo').addEventListener('click', () => photoInput.click());

  photoInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (event) => {
        const src = event.target.result;
        state.photos.push({ date: new Date().toLocaleDateString(), src });
        renderPhotos();
        showToast('Foto adicionada com sucesso!');
      };
      reader.readAsDataURL(file);
    }
  });

  function renderPhotos() {
    photosGrid.innerHTML = '';
    state.photos.forEach(p => {
      const img = document.createElement('img');
      img.src = p.src;
      img.className = 'photo-thumb';
      photosGrid.appendChild(img);
    });

    if (state.photos.length >= 2) {
      const first = state.photos[0].src;
      const last = state.photos[state.photos.length - 1].src;
      
      photoSlider.innerHTML = `
        <img src="${first}" class="photo-img-before">
        <img src="${last}" class="photo-img-after" id="img-after">
        <div class="slider-handle" id="slider-handle">↔</div>
      `;

      // Slider logic
      const handle = document.getElementById('slider-handle');
      const imgAfter = document.getElementById('img-after');
      let isDragging = false;

      handle.addEventListener('mousedown', () => isDragging = true);
      handle.addEventListener('touchstart', () => isDragging = true);
      
      document.addEventListener('mouseup', () => isDragging = false);
      document.addEventListener('touchend', () => isDragging = false);
      
      document.addEventListener('mousemove', (e) => slide(e));
      document.addEventListener('touchmove', (e) => slide(e.touches[0]));

      function slide(e) {
        if (!isDragging) return;
        const rect = photoSlider.getBoundingClientRect();
        let x = e.clientX - rect.left;
        if (x < 0) x = 0;
        if (x > rect.width) x = rect.width;
        let percent = (x / rect.width) * 100;
        
        handle.style.left = percent + '%';
        imgAfter.style.width = percent + '%';
      }
    }
  }

  // --- GOALS ---
  document.getElementById('btn-save-hyper-goals').addEventListener('click', () => {
    showToast('Metas corporais salvas!');
    calcDiet(); // update diet macros based on new weight
  });
  
  // Header Date
  const dateOptions = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  document.getElementById('header-date').textContent = new Date().toLocaleDateString('pt-BR', dateOptions);

  // Initialize
  renderCalendar();

});
