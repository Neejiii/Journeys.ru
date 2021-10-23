create table points
values (
    id uuid not null,
    loc_lat decimal(3, 10) not null,
    loc_long decimal(3, 10) not null,
    text varchar,
)