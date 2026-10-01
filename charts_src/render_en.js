const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const scale = parseFloat(process.argv[2] || '1');
  const names = ['Chart1_Three_conversions_from_Bloom_ramp', 'Chart2_Bloom_inventory_vs_CCTC_sales', 'Chart3_Coverage_and_value_per_GW',
                 'Chart4_Amosense_share_of_Bloom_demand', 'Chart5_CCTC_separator_revenue_scenarios', 'Chart6_Validation_sequence'];
  const heights = Object.fromEntries(fs.readFileSync('heights.txt', 'utf8').trim().split(' ').map(s => s.split(':').map(Number)));
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  fs.mkdirSync('out_en', { recursive: true });
  for (let k = 1; k <= 6; k++) {
    const page = await browser.newPage({ viewport: { width: 1440, height: heights[k] }, deviceScaleFactor: scale });
    await page.goto('file://' + process.cwd() + `/chart${k}_en.html`);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    const suffix = scale > 2 ? '_5K' : '_preview';
    await page.screenshot({ path: `out_en/${names[k - 1]}${suffix}.png`, omitBackground: false });
    await page.close();
  }
  await browser.close();
  console.log('done');
})();
