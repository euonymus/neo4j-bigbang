# -*- coding: utf-8 -*-
import sys
import load_dot_env
from usecases.import_nodes import ImportNodes, ACTION_TYPE_SKIP, ACTION_TYPE_UPDATE

DEFAULT_FILE_NAME = 'nodes.csv'
def main(args = sys.argv):

    action_type = ACTION_TYPE_SKIP
    file_name = DEFAULT_FILE_NAME
    labels_in_row = True
    unique_labels = None
    unique_property_keys = None

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
        if '-f' in args:
            labels_in_row = False

    # unique labels
    # If labels are specified, those are the targeted labels. ( It's used if you want to update labels on targeted Nodes )
    # If no labels are specified, labels in CSV will be targeted.
    if '-l' in args:
        i = args.index('-l')
        if len(args) <= i + 1:
            # raise AttributeError('Unique labels are required.')
            unique_labels = True
        elif args[i + 1].startswith('-'):
            # raise AttributeError('Unique labels are required.')
            unique_labels = True
        else:
            labels = args[i + 1]
            unique_labels = labels.split('|')

    # unique property keys
    if '-p' in args:
        i = args.index('-p')
        if len(args) <= i + 1:
            raise AttributeError('Unique property keys are required.')
        if args[i + 1].startswith('-'):
            raise AttributeError('Unique property keys are required.')
        property_keys = args[i + 1]
        unique_property_keys = property_keys.split('|')

    try:
        import_nodes = ImportNodes(file_name, labels_in_row, unique_labels, unique_property_keys)
        import_nodes.invoke(action_type)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
