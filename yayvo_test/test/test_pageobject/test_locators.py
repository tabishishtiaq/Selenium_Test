class locators(object):

    user_name = "login[username]"
    password = "login[password]"
    signin = "send"
    account_title = "//div[@class='page-title']/h1"
    nav = "//ul[@class= 'nav_bar_list']/li[4]/a"
    acc_info = "//a[contains(text(),'Account Information')]"

    first_name = "//input[@id='firstname']"
    last_name = "//input[@id='lastname']"
    email = "//input[@id='email']"
    cont_nmbr = "//input[@id='mobile']"
    cnic = "//input[@id='customer_cnic']"
    save = "//span[contains(text(),'Save')]"
    notifi_message = "//li[contains(text(),'The account information has been saved.')]"
    address = "//strong[contains(text(),'Address Book')]"

    mywish = "//div[@class='content-l']/ul/li[2]/a"
    nav2 = "//li[@class='last']/a"
    check_out = "//div[@class = 'content-l']/ul/li[3]/a"
    click_here = "//div[@class='cart-empty']/p/a"