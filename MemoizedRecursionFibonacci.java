package fibonacci;

import java.util.HashMap;
import java.util.Map;

public class MemoizedRecursionFibonacci implements Fibonacci {
	private Map<Integer, Integer> fibArray = new HashMap<Integer, Integer>();

  @Override
  public int computeFibonacci(int position) {

    if (fibArray.containsKey(position)) {
      return fibArray.get(position);
    }
    else {
      RecursiveFibonacci computeObject = new RecursiveFibonacci();
      int value = computeObject.computeFibonacci(position);
      fibArray.put(position,value);
      return value;
    }
  }
}


