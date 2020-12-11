from exceptions import InvalidIdFromContextException


def get_id_from_context(context):
    if len(context.args):
        if not context.args[0].isdigit():
            raise InvalidIdFromContextException('Invalid certificate number')
    else:
        raise InvalidIdFromContextException('Invalid data')

    return int(context.args[0])
