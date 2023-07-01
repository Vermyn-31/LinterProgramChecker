typedef struct _settingsItem {
    char *name;
    char *description;
    _settingsItem *next;
} _settingsItem;

class Settings {
    _settingsItem list;
    Settings() {{
        list.name = nullptr;
        list.description = nullptr;
        list.next = nullptr;
    }
}
