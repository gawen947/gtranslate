#!/bin/sh
# This wrapper use translaboob but you may use a different command instead.
translaboob translate "$1" "$2" "$3" | tail -n1
