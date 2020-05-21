class TestLogin:
    def test_login(self, admin_product_page):
        admin_product_page.login_admin()
        # admin_product_page.add_new_product()
        admin_product_page.open_product_tab()
        admin_product_page.delete_product_from_tab()
