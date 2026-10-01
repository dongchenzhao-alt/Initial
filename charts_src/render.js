const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const scale = parseFloat(process.argv[2] || '1');
  const names = ['图表1_Bloom放量的三道换算', '图表2_Bloom存货与三环销售额', '图表3_覆盖率与每GW价值量',
                 '图表4_Amosense占Bloom需求比例', '图表5_三环隔膜片收入情景', '图表6_跟踪验证顺序'];
  const heights = Object.fromEntries(fs.readFileSync('heights.txt', 'utf8').trim().split(' ').map(s => s.split(':').map(Number)));
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  fs.mkdirSync('out', { recursive: true });
  for (let k = 1; k <= 6; k++) {
    const page = await browser.newPage({ viewport: { width: 1440, height: heights[k] }, deviceScaleFactor: scale });
    await page.goto('file://' + process.cwd() + `/chart${k}.html`);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    const suffix = scale > 2 ? '_5K' : '_preview';
    await page.screenshot({ path: `out/${names[k - 1]}${suffix}.png`, omitBackground: false });
    await page.close();
  }
  await browser.close();
  console.log('done');
})();
