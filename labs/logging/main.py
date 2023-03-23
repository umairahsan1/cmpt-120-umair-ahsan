from logger import *
from time import sleep


def main():
    log("main()")
    start()
    log("exiting main()...")
    dump()


def start():
    log("start()")
    authenticate_user()
    run_chef_scripts()
    add_users()
    log("exiting start()...")


def add_users():
    users = []
    for user in ["Kevin", "Anders", "Sophia", "Jessica", "Hayden"]:
        log(f"adding user {user}...")
        sleep(1)
        users += user
        log("added!")


def run_chef_scripts():
    log("running chef scripts...")
    sleep(2)
    log("chef scripts done!")


def authenticate_user():
    log("authenticating...")
    sleep(1)
    log("authenticated!")


main()
