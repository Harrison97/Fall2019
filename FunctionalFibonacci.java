package fibonacci;

import java.util.Collections;
import java.util.stream.Stream;

public class FunctionalFibonacci implements Fibonacci{

  @Override
  public int computeFibonacci(int position) {
    return Stream.iterate(new int[]{1, 1},
            series -> new int[]{series[1], series[0] + series[1]})
            .limit(position)
            .map(series -> series[0])
            .skip(position - 1)
            .findFirst()
            .orElse(1);
  }
}
