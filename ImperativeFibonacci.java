package fibonacci;

public class ImperativeFibonacci implements Fibonacci {

  @Override
  public int computeFibonacci(int position) {
    int previous = 2, current = 3;

    for (int i = 3; i <= position-2; i++) {
      current = previous + current;
      previous = current - previous;
    }

    return current;
  }
}
