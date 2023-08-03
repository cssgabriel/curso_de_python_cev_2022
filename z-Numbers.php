<?php 
class Numbers {
  public $arr = [];

  public function getHighNumber() {
    return max($this->arr);
  }

  public function getSmallNumber() {
    return min($this->arr);
  }

  public function setPushArr(...$n) {
    return array_push($this->arr, ...$n);
  }

  public function getAverage() {
    return array_sum($this->arr) / count($this->arr);
  }

  public function getSum() {
    return array_sum($this->arr);
  }

  public function getCount() {
    return count($this->arr);
  }
}