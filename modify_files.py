import re
import os

app_js_path = r"C:\Users\BRD\Downloads\PS\fittrack\app.js"
style_css_path = r"C:\Users\BRD\Downloads\PS\fittrack\style.css"

with open(app_js_path, "r", encoding="utf-8") as f:
    app_js = f.read()

# 1. Add vectorSvg function
vector_svg_code = """
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
"""
if "function vectorSvg" not in app_js:
    app_js = app_js.replace("document.addEventListener('DOMContentLoaded', () => {", "document.addEventListener('DOMContentLoaded', () => {\n" + vector_svg_code)

# 2. Update exerciseLibrary with svgType and color
exercise_library_old = """  const exerciseLibrary = [
    { cat: 'peito', name: 'Supino Reto na Máquina', muscle: 'Peito', machine: 'SENA Chest Press', exec: 'Sente-se com as costas apoiadas. Empurre as alças para frente estendendo os braços. Retorne controladamente.', err: ['Arquear excessivamente as costas', 'Soltar o peso rápido'] },
    { cat: 'peito', name: 'Peck Deck (Voador)', muscle: 'Peito', machine: 'SENA Pectoral Fly', exec: 'Mantenha os cotovelos alinhados com o peito. Feche os braços contraindo o peitoral.', err: ['Usar muito impulso', 'Cotovelos muito baixos'] },
    { cat: 'costas', name: 'Puxada Frontal', muscle: 'Costas', machine: 'SENA Lat Pulldown', exec: 'Puxe a barra em direção ao peito superior, juntando as escápulas.', err: ['Puxar atrás da nuca', 'Balançar o tronco'] },
    { cat: 'costas', name: 'Remada Sentada', muscle: 'Costas', machine: 'SENA Seated Row', exec: 'Puxe o triângulo até o abdômen, mantendo a postura ereta.', err: ['Curvar as costas'] },
    { cat: 'pernas', name: 'Leg Press 45º', muscle: 'Quadríceps/Glúteos', machine: 'SENA Leg Press', exec: 'Empurre a plataforma sem estender totalmente os joelhos.', err: ['Travar os joelhos no final', 'Descolar a lombar'] },
    { cat: 'pernas', name: 'Cadeira Extensora', muscle: 'Quadríceps', machine: 'SENA Leg Extension', exec: 'Estenda as pernas controladamente. Segure 1s no topo.', err: ['Levantar o quadril'] },
    { cat: 'ombro', name: 'Desenvolvimento Máquina', muscle: 'Ombros', machine: 'SENA Shoulder Press', exec: 'Empurre o peso para cima. Desça até a altura das orelhas.', err: ['Descer demais forçando a articulação'] },
    { cat: 'biceps', name: 'Rosca Scott Máquina', muscle: 'Bíceps', machine: 'SENA Preacher Curl', exec: 'Apoie o tríceps. Flexione os braços isolando o bíceps.', err: ['Tirar os cotovelos do apoio'] },
    { cat: 'triceps', name: 'Tríceps Pulley', muscle: 'Tríceps', machine: 'Polia Alta', exec: 'Estenda os braços para baixo mantendo cotovelos colados ao corpo.', err: ['Afastar cotovelos'] }
  ];"""

exercise_library_new = """  const exerciseLibrary = [
    { cat: 'peito', name: 'Supino Reto na Máquina', muscle: 'Peito', machine: 'SENA Chest Press', exec: 'Sente-se com as costas apoiadas. Empurre as alças para frente estendendo os braços. Retorne controladamente.', err: ['Arquear excessivamente as costas', 'Soltar o peso rápido'], svgType: 'bench', color: '#3b82f6' },
    { cat: 'peito', name: 'Peck Deck (Voador)', muscle: 'Peito', machine: 'SENA Pectoral Fly', exec: 'Mantenha os cotovelos alinhados com o peito. Feche os braços contraindo o peitoral.', err: ['Usar muito impulso', 'Cotovelos muito baixos'], svgType: 'pecdeck', color: '#3b82f6' },
    { cat: 'costas', name: 'Puxada Frontal', muscle: 'Costas', machine: 'SENA Lat Pulldown', exec: 'Puxe a barra em direção ao peito superior, juntando as escápulas.', err: ['Puxar atrás da nuca', 'Balançar o tronco'], svgType: 'lat', color: '#7c3aed' },
    { cat: 'costas', name: 'Remada Sentada', muscle: 'Costas', machine: 'SENA Seated Row', exec: 'Puxe o triângulo até o abdômen, mantendo a postura ereta.', err: ['Curvar as costas'], svgType: 'row', color: '#7c3aed' },
    { cat: 'pernas', name: 'Leg Press 45º', muscle: 'Quadríceps/Glúteos', machine: 'SENA Leg Press', exec: 'Empurre a plataforma sem estender totalmente os joelhos.', err: ['Travar os joelhos no final', 'Descolar a lombar'], svgType: 'legpress', color: '#f97316' },
    { cat: 'pernas', name: 'Cadeira Extensora', muscle: 'Quadríceps', machine: 'SENA Leg Extension', exec: 'Estenda as pernas controladamente. Segure 1s no topo.', err: ['Levantar o quadril'], svgType: 'squat', color: '#f97316' },
    { cat: 'ombro', name: 'Desenvolvimento Máquina', muscle: 'Ombros', machine: 'SENA Shoulder Press', exec: 'Empurre o peso para cima. Desça até a altura das orelhas.', err: ['Descer demais forçando a articulação'], svgType: 'shoulder', color: '#10b981' },
    { cat: 'biceps', name: 'Rosca Scott Máquina', muscle: 'Bíceps', machine: 'SENA Preacher Curl', exec: 'Apoie o tríceps. Flexione os braços isolando o bíceps.', err: ['Tirar os cotovelos do apoio'], svgType: 'curl', color: '#eab308' },
    { cat: 'triceps', name: 'Tríceps Pulley', muscle: 'Tríceps', machine: 'Polia Alta', exec: 'Estenda os braços para baixo mantendo cotovelos colados ao corpo.', err: ['Afastar cotovelos'], svgType: 'tricep', color: '#ef4444' }
  ];"""

app_js = app_js.replace(exercise_library_old, exercise_library_new)

# 3. Update renderExercises
render_exercises_old = """      // Mock animation placeholder using CSS
      card.innerHTML = `
        <div class="lib-anim-placeholder">
          <div class="stick-figure"></div>
        </div>
        <div class="lib-info">
          <div class="lib-name">${ex.name}</div>
          <div class="lib-muscle">${ex.muscle}</div>
        </div>
      `;"""

render_exercises_new = """      card.innerHTML = `
        <div class="ex-anim" style="height:100px; background:var(--surface2); display:flex; align-items:center; justify-content:center;">
          ${vectorSvg(ex.svgType || 'bench', ex.color || '#7c3aed')}
        </div>
        <div class="lib-info">
          <div class="lib-name">${ex.name}</div>
          <div class="lib-muscle">${ex.muscle}</div>
        </div>
      `;"""

app_js = app_js.replace(render_exercises_old, render_exercises_new)

# 4. Update openExerciseDetail
open_exercise_detail_old = """    document.getElementById('tut-execution').textContent = ex.exec;
    
    const errList = document.getElementById('tut-errors');"""

open_exercise_detail_new = """    document.getElementById('tut-execution').textContent = ex.exec;
    
    document.getElementById('tut-animation').innerHTML = vectorSvg(ex.svgType || 'bench', ex.color || '#7c3aed');

    const errList = document.getElementById('tut-errors');"""

app_js = app_js.replace(open_exercise_detail_old, open_exercise_detail_new)

# 5. Update Calendar logic
calendar_old = """  function renderCalendar() {
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();
    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    
    const monthNames = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'];
    calMonthYear.textContent = `${monthNames[month]} ${year}`;
    calGrid.innerHTML = '';

    // Mock data for colors
    const mockWorkouts = {
      2: 'bg-peito',
      4: 'bg-perna',
      6: 'bg-braco',
      9: 'bg-peito',
      11: 'bg-perna',
      14: 'bg-cardio',
      16: 'bg-peito'
    };

    // Blank spaces
    for (let i = 0; i < firstDay; i++) {
      const emptyDiv = document.createElement('div');
      calGrid.appendChild(emptyDiv);
    }

    const today = new Date();

    for (let day = 1; day <= daysInMonth; day++) {
      const dayDiv = document.createElement('div');
      dayDiv.className = 'cal-day active-month';
      dayDiv.textContent = day;

      if (year === today.getFullYear() && month === today.getMonth() && day === today.getDate()) {
        dayDiv.classList.add('today');
      }

      if (mockWorkouts[day]) {
        dayDiv.classList.add(mockWorkouts[day]);
      }

      calGrid.appendChild(dayDiv);
    }
  }"""

calendar_new = """  const calendarSchedule={
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
  }"""

app_js = app_js.replace(calendar_old, calendar_new)

with open(app_js_path, "w", encoding="utf-8") as f:
    f.write(app_js)

# ==================== CSS CHANGES ====================
with open(style_css_path, "r", encoding="utf-8") as f:
    style_css = f.read()

# 1. Update calendar CSS
css_cal_old = """/* CALENDAR */
.calendar-card{padding:1rem;}
.calendar-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;}
.calendar-days-header{display:grid;grid-template-columns:repeat(7,1fr);text-align:center;font-size:0.75rem;color:var(--muted);font-weight:700;margin-bottom:0.5rem;}
.calendar-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:4px;}
.cal-day{aspect-ratio:1;background:var(--surface2);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:0.8rem;color:var(--muted);cursor:pointer;position:relative;}
.cal-day.active-month{color:var(--text);}
.cal-day.today{border:1px solid var(--primary);}
/* Grupos Musculares Cores */
.cal-day.bg-peito{background:rgba(59,130,246,0.3);color:#60a5fa;} /* Azul */
.cal-day.bg-perna{background:rgba(249,115,22,0.3);color:#fb923c;} /* Laranja */
.cal-day.bg-braco{background:rgba(167,139,250,0.3);color:#a78bfa;} /* Roxo */
.cal-day.bg-cardio{background:rgba(16,185,129,0.3);color:#34d399;} /* Verde */
.calendar-legend{display:flex;flex-wrap:wrap;gap:0.8rem;margin-top:1rem;justify-content:center;}
.leg-item{display:flex;align-items:center;gap:4px;font-size:0.75rem;color:var(--muted);}
.leg-dot{width:10px;height:10px;border-radius:50%;}
.color-peito{background:#3b82f6;}
.color-perna{background:#f97316;}
.color-braco{background:#a78bfa;}
.color-cardio{background:#10b981;}
.color-rest{background:var(--surface2);}"""

css_cal_new = """/* CALENDAR */
.calendar-card{padding:1rem;}
.calendar-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;}
.calendar-days-header{display:grid;grid-template-columns:repeat(7,1fr);text-align:center;font-size:0.75rem;color:var(--muted);font-weight:700;margin-bottom:0.5rem;}
.calendar-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:8px;}
.cal-day{height:72px;border-radius:12px;display:flex;flex-direction:column;padding:6px;cursor:pointer;transition:.2s;position:relative;background:var(--surface2);border:1px solid var(--border);overflow:hidden;}
.cal-day:hover{border-color:var(--primary);transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,0.15);}
.cal-empty{background:transparent !important;border:none !important;pointer-events:none;}
.cal-date{font-size:14px;font-weight:700;}
.cal-letter-wrap{width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-family:'Bebas Neue',var(--font);font-size:16px;color:#fff;margin-top:auto;align-self:flex-end;font-weight:bold;}
.cal-rest-wrap{font-size:10px;color:var(--text);margin-top:auto;background:rgba(255,255,255,0.1);padding:2px 6px;border-radius:6px;align-self:flex-end;font-weight:600;}
.cal-day.today{border-color:var(--accent);}
.calendar-legend{display:flex;flex-wrap:wrap;gap:0.8rem;margin-top:1rem;justify-content:center;}
.leg-item{display:flex;align-items:center;gap:4px;font-size:0.75rem;color:var(--muted);}
.leg-dot{width:10px;height:10px;border-radius:50%;}
.color-peito{background:#3b82f6;}
.color-perna{background:#f97316;}
.color-braco{background:#7c3aed;}
.color-cardio{background:#10b981;}
.color-rest{background:rgba(255,255,255,0.1);}"""

style_css = style_css.replace(css_cal_old, css_cal_new)

# 2. Add vector animations
vector_anim_css = """
/* NEW VECTOR ANIMATIONS */
.v-breath { animation: vBreath 3s ease-in-out infinite; transform-origin: center bottom; }
@keyframes vBreath { 0%, 100% { transform: scaleY(1); } 50% { transform: scaleY(1.02) scaleX(0.98); } }
.v-lift { animation: vLift 2s ease-in-out infinite; }
@keyframes vLift { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-12px); } }
.v-pull { animation: vPull 2s ease-in-out infinite; }
@keyframes vPull { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(12px); } }
.v-squat-anim { animation: vSquatAnim 2s ease-in-out infinite; transform-origin: center bottom; }
@keyframes vSquatAnim { 0%, 100% { transform: scaleY(1) translateY(0); } 50% { transform: scaleY(0.85) translateY(10px); } }
.v-row { animation: vRow 2s ease-in-out infinite; }
@keyframes vRow { 0%, 100% { transform: translateX(0); } 50% { transform: translateX(-12px); } }
.v-curl-arm { animation: vCurl 2s ease-in-out infinite; transform-origin: 60px 65px; }
@keyframes vCurl { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(-70deg); } }
.v-legpress { animation: vLegpress 2s ease-in-out infinite; }
@keyframes vLegpress { 0%, 100% { transform: translate(0, 0); } 50% { transform: translate(-12px, 12px); } }
.v-pecdeck { animation: vPecdeck 2s ease-in-out infinite; transform-origin: 60px 40px; }
@keyframes vPecdeck { 0%, 100% { transform: scaleX(1); } 50% { transform: scaleX(0.5); } }
.v-tricep-arm { animation: vTricep 2s ease-in-out infinite; transform-origin: 70px 65px; }
@keyframes vTricep { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(60deg); } }
.v-lateral-arm-l { animation: vLatL 2s ease-in-out infinite; transform-origin: 50px 42px; }
.v-lateral-arm-r { animation: vLatR 2s ease-in-out infinite; transform-origin: 70px 42px; }
@keyframes vLatL { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(-60deg); } }
@keyframes vLatR { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(60deg); } }
.v-shrug-anim { animation: vShrug 2s ease-in-out infinite; transform-origin: center bottom; }
@keyframes vShrug { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-4px); } }
.v-shrug-arms { animation: vShrugArms 2s ease-in-out infinite; }
@keyframes vShrugArms { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
.v-calf-anim { animation: vCalf 2s ease-in-out infinite; transform-origin: center bottom; }
@keyframes vCalf { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
.v-abs-anim { animation: vAbs 2s ease-in-out infinite; transform-origin: 60px 90px; }
@keyframes vAbs { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(20deg); } }
.v-cardio { animation: vCardio 0.6s ease-in-out infinite alternate; }
@keyframes vCardio { 0% { transform: translateY(0); } 100% { transform: translateY(-4px); } }
.v-run-leg-1 { animation: vRunLeg1 1.2s infinite; }
.v-run-leg-2 { animation: vRunLeg2 1.2s infinite; }
.v-run-arm-1 { animation: vRunArm1 1.2s infinite; }
.v-run-arm-2 { animation: vRunArm2 1.2s infinite; }
@keyframes vRunLeg1 { 0%, 100% { transform: rotate(-25deg); } 50% { transform: rotate(25deg); } }
@keyframes vRunLeg2 { 0%, 100% { transform: rotate(25deg); } 50% { transform: rotate(-25deg); } }
@keyframes vRunArm1 { 0%, 100% { transform: rotate(25deg); } 50% { transform: rotate(-25deg); } }
@keyframes vRunArm2 { 0%, 100% { transform: rotate(-25deg); } 50% { transform: rotate(25deg); } }
"""
if "/* NEW VECTOR ANIMATIONS */" not in style_css:
    style_css += "\n" + vector_anim_css

with open(style_css_path, "w", encoding="utf-8") as f:
    f.write(style_css)

print("Done updating app.js and style.css")
