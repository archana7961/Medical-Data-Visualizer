def test_draw_cat_plot():
    from medical_data_visualizer import draw_cat_plot
    assert draw_cat_plot() is not None

def test_draw_heat_map():
    from medical_data_visualizer import draw_heat_map
    assert draw_heat_map() is not None
