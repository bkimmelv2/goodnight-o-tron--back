# Goodnight-o-Tron API
## An app for all of your bedtime reading needs!
Do you have children who like to read bedtime stories? Are you sick of having to pick the books out yourself every single night? Well I have the solution for you! The Goodnight-o-Tron is a simple app to make bedtime reading a breeze. Simply load in the collection of books you have at home and hit GENERATE on the home page. This will select two books at random for you to read to your little one. After reading time is over, you have the option to leave a brief note about that specific reading experience. This will also record the date you read the book as well as an attention score from 1-5 that you can use to gauge how interested your child was at that moment. Once a note is submitted, it can be viewed on the All Notes screen. Opening an individual Book entry in your Library will also show all notes associated with that book.

Save some memories and make bedtime easy with the Goodnight-o-Tron!

[Goodnight-o-Tron App](https://goodnight-o-tron.netlify.app/)

## Fetch Endpoints
- API URL (in React: REACT_APP_BACKEND_URL): `https://goodnight-o-tron-7228c2d6cff7.herokuapp.com`

- GET /random/ will grab two random books from the database.
- GET /books/ will show the current library of books.
- GET /books/id/ will show a separate page of the title, image, all notes of the selected book.
- POST /books/ will allow the user to add a book title/image to their library.
- PUT /books/id/ will allow the user to edit a specified book's details.
- DELETE /books/id/ will allow the user to delete a book from their library.
- GET /notes/ will show all notes ever created, sorted by date added.
- GET /notes/id/ will show a specific note's details.
- POST /notes/ will allow the user to add a note to a book after it has been generated.
- PUT /notes/id/ will allow the user to edit a specific note.
- DELETE /notes/id/ will allow the user to delete a specific note.