from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    return 'Ошибка 404'
