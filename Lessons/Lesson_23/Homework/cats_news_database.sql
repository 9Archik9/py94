create DATABASE Cats_News;

\c Cats_News

create TABLE news (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    picture VARCHAR(255),
    rating INT,
    /* rating may be negative.
    we agreed that this is a display of the ratio of likes to dislikes in one num
    */
    comment TEXT,
    popularity INT,
    CONSTRAINT check_positive_popularity CHECK (popularity >= 0)
);

create TABLE comments (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    nickname VARCHAR(255) NOT NULL,
    "like" INT,
    dislike INT,
    news_id INTEGER REFERENCES news(id),
    parent_comment_id INTEGER REFERENCES comments(id), -- tree structure of comments. recursive relation
    CONSTRAINT check_positive_like CHECK ("like" >= 0),
    CONSTRAINT check_positive_dislike CHECK (dislike >= 0) -- is it two CONSTRAINT are necessary?
);
