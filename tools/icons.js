// Gera os ícones PNG do aplicativo (192 e 512 px) a partir de images/favicon.svg,
// o mesmo ícone do site. Rodar só quando o favicon mudar:
//   node tools/icons.js
// Usa o Chromium do Playwright para desenhar o SVG; os PNG ficam em images/ e
// entram no repositório, para a build não depender de navegador.
const {chromium} = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const root = path.dirname(__dirname);
  const svg = fs.readFileSync(path.join(root, 'images/favicon.svg'), 'utf8');
  const b = await chromium.launch();
  for (const n of [192, 512]) {
    const p = await b.newPage({viewport: {width: n, height: n}});
    await p.setContent(`<html><body style="margin:0;background:transparent">${svg.replace('<svg ', `<svg width="${n}" height="${n}" `)}</body></html>`);
    await p.screenshot({path: path.join(root, `images/icon-${n}.png`), omitBackground: true});
    console.log('images/icon-' + n + '.png');
  }
  await b.close();
})();
