from controllers import pepe_controller, ether_delta_controller

def bind_routes(application):
    """Bind the routes onto the application instance"""
    
    # 4chan
    application.add_url_rule('/4chan/boards', 'get_board_page', pepe_controller.get_board_page)
    application.add_url_rule('/4chan/threads', 'get_thread', pepe_controller.get_thread)

    ether_delta_controller.connect()


