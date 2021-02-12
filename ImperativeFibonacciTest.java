package fibonacci;

import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Mode;

public class ImperativeFibonacciTest implements FibonacciTest {

  @Override
  public Fibonacci createFibonacci() {
    return new ImperativeFibonacci();
  }

  @Benchmark
  @BenchmarkMode(Mode.AverageTime)
  @Override
  public void fibonacciPerformance()
  {
    fibonacciTest();
  }

}
