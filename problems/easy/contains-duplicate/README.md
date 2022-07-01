# contains-duplicate

speed: set_len > hash_map > hash_set

That's because the hash_set solution has multiple lookups into the Set.

hash_map is ok because the Entry API is prime.

set_len is dope, could change the from_iter into collect tho.

Lessons learned:

1. Sets are useful for checking duplicates.
