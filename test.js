import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();

  // Переходим на страницу логина Adminer
  await page.goto('http://adminer:8080');

  // Выбираем систему PostgreSQL
  await page.select('select[name="auth[driver]"]', 'pgsql');

  // Заполняем поля: Сервер, Пользователь, Пароль
  await page.type('input[name="auth[server]"]', 'postgres');
  await page.type('input[name="auth[username]"]', 'postgres');
  await page.type('input[name="auth[password]"]', process.env.DB_PASS);

  // Жмем кнопку "Войти" и ждем, пока страница обновится
  await Promise.all([
    page.waitForNavigation(),
    page.click('input[type="submit"]')
  ]);

  // Делаем скриншот после успешного входа
  await page.screenshot({ path: 'adminer_logged_in.png' });
  console.log('Успешный вход! Скриншот adminer_logged_in.png сохранен.');

  await browser.close();
})();
