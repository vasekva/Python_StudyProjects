TEMPLATE_PATH = "Input\\Letters\\starting_letter.txt"
NAMES_PATH = "Input\\Names\\invited_names.txt"
INVITE_FILE_PATH = "Output\\ReadyToSend"


def read_template() -> str:
    with open(TEMPLATE_PATH) as template_file:
        return template_file.read()


def get_invited_names() -> list[str]:
    with open(NAMES_PATH) as names_file:
        return [line.strip() for line in names_file.readlines()]


template_str = read_template()
invited_names = get_invited_names()

for guest_name in invited_names:
    invite = template_str.replace("[name]", guest_name)
    with open(f"{INVITE_FILE_PATH}\\letter_for_{guest_name}.txt", mode='w') as invite_file:
        invite_file.write(invite)
