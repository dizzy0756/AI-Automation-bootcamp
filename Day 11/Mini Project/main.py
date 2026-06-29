import utils
from model import Post

while True:
    print("--------------------Menu------------------------")
    print("1. View Posts")
    print("2. View Users")
    print("3. Search Post by User Id")
    print("4. Create Post")
    print("5. Exit")
    print("--------------------Menu------------------------")

    while True:
        try:
            choice = int(input("Choose an option"))
            break
        except ValueError:
            print("Invalid Option")

    if choice == 5:
        break

    match choice:
        case 1:
            utils.view_post()
        case 2:
            utils.view_users()
        case 3:
            user_id = int(input("Enter the user_id of the post you want to search : "))
            utils.search_post(user_id)
        case 4:
            user_id = int(input("Enter the user_id of the post you want to create : "))
            title = input("Enter the title of the post you to want create : ")
            body = input("Enter the body of the post : ")
            post = Post(user_id,title,body)
            new_post = utils.create_post(post)
            new_post.display()

