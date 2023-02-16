import os


class IconValidator:

    def __init__(self, theme_soup, theme_location):

        self.soup = theme_soup
        self.theme_location = theme_location

    def validate(self):
        """
        Check if all icons(symbols) defined in the base xml are available in the theme folder
        Missing icons are reported in txt file "missing_icons.txt"
        """
        icon_paths = self._get_icon_paths()
        missing_icons = []
        for icon in icon_paths:
            full_path = os.path.normpath(os.path.join(os.path.dirname(self.theme_location), icon))
            if not os.path.exists(full_path):
                if icon not in missing_icons:
                    missing_icons.append(icon)

    def _write_missing_icons_to_file(self, missing_icons):
        """
        Write all missing icons into text file
        :param missing_icons:
        """
        log_file = 'missing_icons.txt'

        # remove file if exist
        if os.path.exists(log_file):
            os.remove(log_file)

        if len(missing_icons) > 0:
            # sort alphabetically the icons paths
            missing_icons.sort()
            with open(log_file, 'w') as f:
                f.writelines('\n'.join(missing_icons))

            print("WARNING: the theme contains definition of symbols that doesn't exist in theme folder. Check " +
                  "missing icons in text file: {}".format(log_file))

    def _get_icon_paths(self) -> list:
        """
        Find all references to external icon (files)
        :return: list of local path used as sources for symbols
        """
        paths = []
        for tag in self.soup.select('[src]'):
            if tag['src'].startswith('file:'):
                paths.append(tag['src'].replace('file:/', '').replace('file:', ''))
        return paths
