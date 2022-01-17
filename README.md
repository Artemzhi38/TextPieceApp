# TextPieceApp
Web service student-project for indexing and searching TextPieces objects.
Uses FastAPI framework and ElasticSearch engine.

## Installation
To run service use docker-compose commands:

**docker-compose build** to build an image.

**docker-compose up** to run the container.


Now the web service can be accessed with through your browser with *localhost*. 
To try service (saving and searching processes) use *localhost/docs*.

## Indexing

To save exact TextPiece click on **POST** section. 
Then click on button **Try it out** and fetch your TextPiece in the **Request body** section below.
Click **Execute** button.

## Searching

To search among indexed TextPieces click on **GET** section, then click on button **Try it out**.

Fill the fields in the section below and click "Execute" button for parametrized search.

If You want to see all indexed TextPieces, leave the fields unfilled. 
