<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Pedido especial 💕</title>
<style>
  :root {
    --bg: #ffc8e0;
    --fg: #3a1a2a;
    --btn: #f4a3b8;
    --btn-fg: #3a1a2a;
    box-sizing: border-box;
    padding-top: env(safe-area-inset-top, 0px);
    padding-bottom: env(safe-area-inset-bottom, 0px);
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --bg: #3a1a2a;
      --fg: #ffc8e0;
      --btn: #8a3d5c;
      --btn-fg: #ffe6f1;
    }
  }
  :root[data-theme="dark"] {
    --bg: #3a1a2a;
    --fg: #ffc8e0;
    --btn: #8a3d5c;
    --btn-fg: #ffe6f1;
  }
  html { scroll-padding-top: env(safe-area-inset-top, 0px); height: 100%; }
  html, body { margin: 0; }
  body {
    height: 100%;
    background: var(--bg);
    color: var(--fg);
    font-family: "Poppins", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    overflow: hidden;
    touch-action: manipulation;
  }
  main { padding: 24px; }
  h1 { font-size: clamp(1.6rem, 6vw, 2.4rem); margin: 0 0 32px; }
  .botoes { display: flex; gap: 20px; justify-content: center; align-items: center; }
  button {
    font: inherit;
    font-weight: 700;
    font-size: 1.1rem;
    padding: 12px 28px;
    border: 0;
    border-radius: 10px;
    background: var(--btn);
    color: var(--btn-fg);
    cursor: pointer;
    transition: transform .15s ease, left .15s ease, top .15s ease;
  }
  #sim { transform-origin: center; }
  #nao { white-space: nowrap; }
  #final { font-size: clamp(2rem, 9vw, 3.5rem); font-weight: 800; }
  .coracao {
    position: fixed;
    bottom: -40px;
    animation: subir linear forwards;
    pointer-events: none;
  }
  @keyframes subir {
    to { transform: translateY(-110vh); opacity: .2; }
  }
</style>
</head>
<body>
<main id="tela">
  <h1>Quer namorar comigo?</h1>
  <div class="botoes">
    <button id="sim">Sim</button>
    <button id="nao">Não</button>
  </div>
</main>

<script>
  var sim = document.getElementById('sim');
  var nao = document.getElementById('nao');
  var tela = document.getElementById('tela');
  var frases = ['Não', 'Tem certeza?', 'Pensa direito…', 'Olha o Sim ali!', 'Última chance!', 'Não adianta!'];
  var fugas = 0;
  var ultimo = { x: -999, y: -999 };

  function fugir(e) {
    if (e && e.cancelable) e.preventDefault();
    if (e && e.clientX !== undefined) { ultimo = { x: e.clientX, y: e.clientY }; }
    else if (e && e.touches && e.touches[0]) { ultimo = { x: e.touches[0].clientX, y: e.touches[0].clientY }; }

    fugas++;
    nao.textContent = frases[fugas % frases.length];
    nao.style.position = 'fixed';

    var w = nao.offsetWidth, h = nao.offsetHeight;
    var margem = 12;
    var maxX = Math.max(margem, window.innerWidth - w - margem);
    var maxY = Math.max(margem, window.innerHeight - h - margem);
    var x, y, tentativas = 0;
    do {
      x = margem + Math.random() * (maxX - margem);
      y = margem + Math.random() * (maxY - margem);
      tentativas++;
    } while (tentativas < 12 &&
             Math.hypot(x + w / 2 - ultimo.x, y + h / 2 - ultimo.y) < 140);

    nao.style.left = x + 'px';
    nao.style.top = y + 'px';

    // o Sim cresce a cada fuga
    var escala = Math.min(1 + fugas * 0.12, 2.2);
    sim.style.transform = 'scale(' + escala + ')';
  }

  nao.addEventListener('pointerenter', fugir);
  nao.addEventListener('touchstart', fugir, { passive: false });
  nao.addEventListener('pointerdown', fugir);
  nao.addEventListener('click', fugir);

  function coracoes() {
    var emojis = ['💖', '💕', '💗', '💘', '❤️'];
    for (var i = 0; i < 40; i++) {
      var c = document.createElement('div');
      c.className = 'coracao';
      c.textContent = emojis[Math.floor(Math.random() * emojis.length)];
      c.style.left = Math.random() * 100 + 'vw';
      c.style.fontSize = (18 + Math.random() * 28) + 'px';
      c.style.animationDuration = (3 + Math.random() * 3) + 's';
      c.style.animationDelay = (Math.random() * 1.5) + 's';
      document.body.appendChild(c);
    }
  }

  sim.addEventListener('click', function () {
    nao.remove();
    tela.innerHTML = '<div id="final">Eu sabia! 💖</div>';
    coracoes();
  });
</script>
</body>
</html>
