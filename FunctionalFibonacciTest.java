package fibonacci;

import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Mode;

public class FunctionalFibonacciTest implements FibonacciTest {
	
  @Override
  public Fibonacci createFibonacci() {
    return new FunctionalFibonacci();
  }



}
