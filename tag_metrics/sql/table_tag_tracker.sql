CREATE TABLE tag_tracker (
  idtag_tracker BIGSERIAL PRIMARY KEY,
  tag_id VARCHAR(1024) NOT NULL,
  antenna VARCHAR(1024) NOT NULL,
  reader VARCHAR(1024) NOT NULL,
  status INT NOT NULL,
  updated_time timestamp with time zone NOT NULL,
  created_time timestamp with time zone NOT NULL
);
