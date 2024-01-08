start
break *main+709
commands
	silent
	set $local_variable = *(unsigned long long*)($rbp - 0x18)
	printf "Current value: %llx\n", $local_variable
	continue
end
continue
