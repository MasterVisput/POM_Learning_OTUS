class TestLogin:
    def test_add_new_pruduct(self, admin_product_page):
        admin_product_page.add_new_product(p_name='Mouse', m_tag='pereferi')
        assert admin_product_page.is_product_in_tab(p_name='Mouse'), 'Продукта нет в таблице продуктов'

    def test_delete_product_by_name(self, admin_product_page, setup):
        admin_product_page.delete_product_from_tab(p_name='Mouse')
        assert not admin_product_page.is_product_in_tab(p_name='Mouse'), 'Продукт есть в таблице продуктов'

    def test_edit_product_by_name(self, admin_product_page, setup):
        admin_product_page.edit_product_from_tab(p_name='Mouse', new_p_name='Mouse+21')
        assert admin_product_page.is_product_in_tab(p_name='Mouse+21'), 'Продукт не отредактирован таблице продуктов'
