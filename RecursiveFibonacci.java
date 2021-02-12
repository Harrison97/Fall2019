package fibonacci;

public class RecursiveFibonacci implements Fibonacci {

  @Override
  public int computeFibonacci(int position) {

    return compute(position - 1) + compute(position - 2);
  }
}
