function createArray(numbers)
{
	while(numbers.slice(-1) == ' ')
	{
		numbers.substring(0, numbers.length - 1)
	};
	
	return numbers.split(' ');
};

function isArithmetical(numbers)
{
	var arr = createArray(numbers);
	var d = 0;
	var el = 0;
	var isArithmetical = 0;
	
	if (arr.length < 2)
	{
		console.log('You have not entered numbers');
	}
	else
	{
		d = parseFloat(arr[1] - arr[0]);
		el = parseFloat(arr[0]);
		
		for(var i = 0; i < arr.length; i++)
		{
			if(arr[i] == el)
			{
				el = el + d;
			}
			else
			{
				isArithmetical += 1;
			};
		};
		
		if(isArithmetical == 0)
		{
			console.log("The entered numbers it's arithmetic progression");
		}
		else
		{
			console.log("The entered numbers it's not arithmetic progression");
		};
	};
};