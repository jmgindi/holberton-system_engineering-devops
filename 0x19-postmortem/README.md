# Postmortem - a misspelled extension

Surprise! This isn't a README at all, but is instead a fake postmortem I wrote for practice!

Gotcha.

## Issue Summary
At 00:00, after our most recent WordPress server deploy, our servers were discovered to be returning 500 errors upon all requests, instead of GET requests returning the simple WordPress site it should've been.

## Timeline
00:00 - issue was detected by a lead developer

00:05 - ticket 0x19 was opened by the developer

00:10 - ticket was responded to by Jack Gindi, SRE

00:11 - `ps aux` showed apache processes were running correctly. strace was attached to apache's PID

00:12 - `curl -sI` showed the expected 500 error, and strace logs were checked. A reference to one of the php files was returning a `-1 ENOENT` error. It was discovered that the file in question was being referred to with the extension `.phpp`.

00:13 - removed extra 'p' from the extension using `sed` to make it `.php`, the correct extension for the file. `curl`ing the server now responded with a 200 and the correct site.

00:16 - finished puppet manifest to push the file change to other servers

00:18 - after running `puppet apply`, the other servers began giving the correct responses as well.

## Corrective/Preventative measures

This problem could have been avoided entirely through CI software and unit testing. Rather than pushing untested code to production, we should integrate pre-testing into our workflow.
