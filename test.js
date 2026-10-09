const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.goto('http://adminer:8080');
  await page.screenshot({ path: 'adminer_screenshot.png' });
  await browser.close();
  console.log('Скриншот успешно сохранен!');
})();
