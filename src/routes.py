from controllers import pepe_controller

def bind_routes(application):
    """Bind the routes onto the application instance"""
    
    # 4chan
    application.add_url_rule('/4chan', 'get_board_page', pepe_controller.get_board_page)



