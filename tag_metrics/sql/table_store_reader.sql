CREATE TABLE store_reader (
  idstore_reader BIGINT NOT NULL PRIMARY KEY,
  reader VARCHAR(1024) NOT NULL,
  store VARCHAR(1024) NOT NULL,
  status INT NOT NULL,
  updated_time timestamp with time zone NOT NULL,
  created_time timestamp with time zone NOT NULL
);
