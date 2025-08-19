from tmdb_app.functions import *
import argparse

def main():
    parser = argparse.ArgumentParser(prog="tmdb-app")

    parser.add_argument(
        "--type",
        choices=["playing", "popular", "top", "upcoming", "search"],
        required=True
    )

    parser.add_argument("--name")

    args = parser.parse_args()

    if args.type == "search" and  not args.name:
        parser.error("--name is required when --type is 'search'")

    match args.type:
        case "playing":
            upcoming_movies()
        
        case "popular":
            popular_movies()

        case "top":
            top_rated_movies()

        case "upcoming":
            upcoming_movies()

        case "search":
            search(args.name)



if __name__ == "__main__":
    main()