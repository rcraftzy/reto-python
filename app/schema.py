instructions = [
    'DROP TABLE IF EXISTS joke;',
    """
        CREATE TABLE joke (
            number INT PRIMARY KEY AUTO_INCREMENT,
            value TEXT NOT NULL
        );
    """
]

