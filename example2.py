from treep import util, filters


if __name__ == '__main__':
    test_dir = '/home/vagrant/dotfiles/'
    # test_dir = '/python'
    filter_options = util.FilterOptions(fuzzy_include_dir=True)
    filter_options.set_basedir(test_dir)
    start_tree = util.build_tree(test_dir, filter_options)
    filts = [
        filters.IgnoreDir(['.git']),
        filters.EndsWith('.sh'),
        # filters.FuzzyMatch('f'),
    ]
    filtered_tree = util.apply_filters(start_tree, filts, filter_options)
    util.print_tree(filtered_tree, filter_options)
