// Renders the sketchnote HTML files to PNG. Usage: node render.js
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 1000 }, deviceScaleFactor: 2 });
  for (const name of ['assessors-sketchnote', 'admin-team-sketchnote', 'action-plan-sketchnote']) {
    await page.goto('file://' + path.join(__dirname, name + '.html'));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(500);
    await page.screenshot({ path: path.join(__dirname, name + '.png'), fullPage: true });
    console.log('rendered', name);
  }
  await browser.close();
})();
