-- Examples of setting general location
-- update hosts set lat = 37.224044, lon = -80.420481 where lat = 0;
-- update hosts set lat = 37.224044, lon = -80.420481 where address << '172.16.0.0/12';

-- Example of setting more specific location
-- Put an entire subdomain in one building (as an example)
-- update hosts set lat = 37.224044, lon = -80.420481 where name like '%.foo.bar.example.com';

-- Example of setting very specific location
-- Put a single host in one specific location (as an example)
-- update hosts set lat = 37.224044, lon = -80.420481 where name = 'host.foo.bar.example.com';
-- update hosts set lat = 37.224044, lon = -80.420481 where address = '192.168.1.1';
