package fibonacci;

public interface Fibonacci {
  default int compute(int position)
  {
    if (position < 0) {
      throw new IllegalArgumentException(
      "Position requires a positive number.");
    }

    if (position <= 2) {
      return 1;
    }

    return computeFibonacci(position);

  }

  int computeFibonacci(int position);


}
