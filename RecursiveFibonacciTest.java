package fibonacci;

import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Mode;

public class RecursiveFibonacciTest implements FibonacciTest {

  @Override
  public Fibonacci createFibonacci() {
    return new RecursiveFibonacci();
  }

  @Benchmark
  @BenchmarkMode(Mode.AverageTime)
  @Override
  public void fibonacciPerformance()
  {
    fibonacciTest();
  }
}
