# -*- coding: utf-8 -*-
import sys
import load_dot_env
from usecases.import_relationships import ImportRelationships, ACTION_TYPE_SKIP, ACTION_TYPE_UPDATE

DEFAULT_FILE_NAME = 'relationships.csv'
def main(args = sys.argv):

    action_type = ACTION_TYPE_SKIP
    file_name = DEFAULT_FILE_NAME
    type_in_row = True
    create_node = False

    # Update or Skip
    if '-u' in args:
        i = args.index('-u')
        action_type = ACTION_TYPE_UPDATE
        # del args[i]

    # File Name Specification
    if '-n' in args:
        i = args.index('-n')
        if len(args) <= i + 1:
            raise AttributeError('file_name is required.')
        if args[i + 1].startswith('-'):
            raise AttributeError('file_name is required.')
        file_name = args[i + 1]
        if '-a' in args:
            type_in_row = False

    # Create Node if not exists
    if '-c' in args:
        i = args.index('-c')
        create_node = True

    try:
        import_relationships = ImportRelationships(file_name, type_in_row, create_node)
        import_relationships.invoke(action_type)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
