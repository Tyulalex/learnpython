
class CustomPreferences:

    class __CustomPreference:
        color = 'Green'

    instance = None

    @classmethod
    def me(cls):
        return CustomPreferences()

    def __new__(cls):
        if not CustomPreferences.instance:
            CustomPreferences.instance = CustomPreferences.__CustomPreference()
        return CustomPreferences.instance

   # def __getattr__(self, item):
   #     getattr(self.instance, item)

   # def __setattr__(self, key, value):
   #     setattr(self.instance, key, value)

custom_preference = CustomPreferences.me()
print(custom_preference.color)

custom_preference.color = 'Red'

custom_preference = CustomPreferences.me()
print(custom_preference.color)
