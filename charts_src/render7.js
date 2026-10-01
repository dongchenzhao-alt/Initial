const { chromium } = require('playwright');
(async () => {
  const scale = parseFloat(process.argv[2] || '1');
  const jobs = [['chart7.html', 'out/图表7_财务模型汇总表', parseInt(process.argv[3])], ['chart7_en.html', 'out_en/Chart7_Financial_model_summary', parseInt(process.argv[4])]];
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  for (const [f, out, h] of jobs) {
    const page = await browser.newPage({ viewport: { width: 1440, height: h }, deviceScaleFactor: scale });
    await page.goto('file://' + process.cwd() + '/' + f);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    const th = await page.evaluate(() => document.querySelector('.tb').getBoundingClientRect().bottom);
    const H = Math.ceil(th + 105);
    await page.evaluate((H) => { document.documentElement.style.height = H + 'px'; document.body.style.height = H + 'px'; }, H);
    await page.setViewportSize({ width: 1440, height: H });
    console.log(f, 'table bottom', th, 'page', H);
    await page.screenshot({ path: `${out}${scale > 2 ? '_5K' : '_preview'}.png` });
    await page.close();
  }
  await browser.close();
})();
