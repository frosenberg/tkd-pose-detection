# Start my GPU-enabled dev VM. It assumes the az CLI is logged in and the 
# subscription is set correctly. 

#!/bin/sh

az vm start -g frosenberg-rg -n aibox