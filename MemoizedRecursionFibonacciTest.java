package fibonacci;

import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Mode;

public class MemoizedRecursionFibonacciTest implements FibonacciTest {
	
  @Override
  public Fibonacci createFibonacci() {
    return new MemoizedRecursionFibonacci();
  }

  @Benchmark
  @BenchmarkMode(Mode.AverageTime)
  @Override
  public void fibonacciPerformance()
  {
    fibonacciTest();
  }

}
