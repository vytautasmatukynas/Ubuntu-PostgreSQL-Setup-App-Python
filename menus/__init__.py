from psql_actions.psql_install import SetupClass
from psql_actions.psql_version_status import VersionClass
from psql_actions.psql_service_actions import ServiceClass
from colors import Color


class Menu:

    @classmethod
    def main_menu(cls):
        """ Main menu selection """
        while True:
            print(Color.LIGHT_GREEN +
                  "--> Setup for PostgreSQL on Ubuntu <--"
                  + Color.DEFAULT)

            action = input(Color.YELLOW
                           + "Choose the action number you want to perform:"
                           + Color.DEFAULT +
                           "\n1. Setup PostgreSQL."
                           "\n2. PostgreSQL service."
                           + Color.RED
                           + "\n3. Exit."
                           + Color.DARK_GREEN
                           + "\nStart action: "
                           + Color.DEFAULT)

            match action:
                case "1":
                    # PostgreSQL Setup
                    cls.install_menu()
                case "2":
                    # PostgreSQL Service Actions
                    cls.actions_menu()
                case "3":
                    print(Color.RED
                          + "\n--> Exiting... <--\n"
                          + Color.DEFAULT)
                    break
                case _:
                    print(Color.RED
                          + "\nInvalid choice. Please enter a valid number.\n"
                          + Color.DEFAULT)
                    continue

    @classmethod
    def install_menu(cls):
        """ Install PSQL menu selection """
        while True:
            print(Color.LIGHT_GREEN +
                  "\n--> Setup PostgreSQL <--"
                  + Color.DEFAULT)

            action = input(Color.YELLOW
                           + "Choose the action number you want to perform:"
                           + Color.DEFAULT +
                           "\n1. Download GPG key."
                           "\n2. Add repository."
                           "\n3. Install PostgreSQL."
                           + Color.BLUE
                           + "\n4. Execute all actions to install."
                           + Color.DEFAULT +
                           "\n5. Check PostgreSQL status."
                           "\n6. Check PostgreSQL version."
                           + Color.RED
                           + "\n7. Exit."
                           + Color.DARK_GREEN
                           + "\nStart action: "
                           + Color.DEFAULT)

            match action:
                case "1":
                    SetupClass().download_postgresql_key()
                case "2":
                    SetupClass().add_postgresql_repository()
                case "3":
                    SetupClass().install_postgresql()
                case "4":
                    SetupClass().exec_postgresql_install()
                case "5":
                    VersionClass().get_postgresql_status()
                case "6":
                    VersionClass().get_postgresql_version()
                case "7":
                    print(
                        Color.RED
                        + "\n--> Exiting PostgreSQL setup... <--\n"
                        + Color.DEFAULT)
                    break

                case _:
                    print(
                        Color.RED
                        + "\nInvalid choice. Please enter a valid number.\n"
                        + Color.DEFAULT)
                    continue

    @classmethod
    def actions_menu(cls):
        """ Actions with PSQL menu selection """
        while True:
            print(Color.LIGHT_GREEN +
                  "\n--> PostgreSQL service enable/disable <--"
                  + Color.DEFAULT)

            action = input(Color.YELLOW
                           + "Choose the action number you want to perform:"
                           + Color.DEFAULT +
                           "\n1. Enable PostgreSQL service."
                           "\n2. Start PostgreSQL service."
                           + Color.RED
                           + "\n3. Stop PostgreSQL service."
                           + Color.BLUE
                           + "\n4. Restart PostgreSQL service."
                           + Color.DEFAULT +
                           "\n5. Check PostgreSQL status."
                           "\n6. Check PostgreSQL version."
                           + Color.RED
                           + "\n7. Exit."
                           + Color.DARK_GREEN
                           + "\nStart action: "
                           + Color.DEFAULT)

            match action:
                case "1":
                    ServiceClass().enable_postgresql_service()
                case "2":
                    ServiceClass().start_postgresql_service()
                case "3":
                    ServiceClass().stop_postgresql_service()
                case "4":
                    ServiceClass().restart_postgresql_service()
                case "5":
                    VersionClass().get_postgresql_status()
                case "6":
                    VersionClass().get_postgresql_version()
                case "7":
                    print(Color.RED
                          + "\n--> Exiting PostgreSQL service... <--\n"
                          + Color.DEFAULT)
                    break
                case _:
                    print(Color.RED
                          + "\nInvalid choice. Please enter a valid number.\n"
                          + Color.DEFAULT)
                    continue
