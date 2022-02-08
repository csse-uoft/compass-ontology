from owlready2 import Thing, default_world, CURRENT_NAMESPACES


def get_class(class_name, ns=None, class_type=(Thing,)):
    """
    Get the class, create it if not yet created.
    This helper prevents the recursive references/imports.
    """
    if not isinstance(class_type, tuple):
        class_type = (class_type, )

    # Support 'with namespace:' block
    found_class = (ns and ns[class_name]) or \
                  (CURRENT_NAMESPACES.get()
                   and len(CURRENT_NAMESPACES.get())
                   and CURRENT_NAMESPACES.get()[-1][class_name])
    if found_class:
        return found_class

    new_class = type(class_name, class_type, {
        'namespace': ns
    })
    return new_class
